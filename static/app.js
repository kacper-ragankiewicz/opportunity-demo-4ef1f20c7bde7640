const summaryEl = document.getElementById('summary');
const itemsEl = document.getElementById('items');
const messageEl = document.getElementById('message');
const statusFilterEl = document.getElementById('statusFilter');

function label(value) {
  return value.replace('_', ' ');
}

function renderSummary(summary) {
  summaryEl.innerHTML = Object.entries(summary)
    .map(([key, value]) => `
      <article class="card summary-card">
        <strong>${label(key)}</strong>
        <span>${value}</span>
      </article>`)
    .join('');
}

function renderItems(items) {
  if (!items.length) {
    itemsEl.innerHTML = '';
    messageEl.textContent = 'No work items match this filter.';
    return;
  }

  messageEl.textContent = `${items.length} item(s)`;
  itemsEl.innerHTML = items.map(item => `
    <article class="card item-card">
      <div class="row">
        <h2>${item.title}</h2>
        <span class="pill">${label(item.status)}</span>
      </div>
      <p>Owner: ${item.owner}</p>
      <p>Priority: ${item.priority}</p>
    </article>`).join('');
}

async function loadItems() {
  const params = new URLSearchParams();
  if (statusFilterEl.value) params.set('status', statusFilterEl.value);

  messageEl.textContent = 'Loading…';
  itemsEl.innerHTML = '';

  const suffix = params.toString() ? `?${params.toString()}` : '';
  const response = await fetch(`/api/work-items${suffix}`);
  const payload = await response.json();

  if (!response.ok) {
    summaryEl.innerHTML = '';
    messageEl.textContent = `Error: ${payload.error}`;
    return;
  }

  renderSummary(payload.summary);
  renderItems(payload.items);
}

statusFilterEl.addEventListener('change', () => {
  loadItems().catch(() => {
    summaryEl.innerHTML = '';
    itemsEl.innerHTML = '';
    messageEl.textContent = 'Request failed.';
  });
});

loadItems().catch(() => {
  summaryEl.innerHTML = '';
  itemsEl.innerHTML = '';
  messageEl.textContent = 'Request failed.';
});
