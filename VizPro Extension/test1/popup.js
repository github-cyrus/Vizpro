function updateTabTimes() {
  chrome.runtime.sendMessage({ type: 'getTabTimes' }, (response) => {
    const tabTimesTableBody = document.getElementById('tabTimesTable').getElementsByTagName('tbody')[0];
    tabTimesTableBody.innerHTML = '';

    for (const [tabId, timeSpent] of Object.entries(response)) {
      const row = document.createElement('tr');
      const tabIdCell = document.createElement('td');
      const timeSpentCell = document.createElement('td');

      tabIdCell.textContent = tabId;
      timeSpentCell.textContent = (timeSpent / 1000).toFixed(2);

      row.appendChild(tabIdCell);
      row.appendChild(timeSpentCell);
      tabTimesTableBody.appendChild(row);
    }
  });
}

document.addEventListener('DOMContentLoaded', updateTabTimes);