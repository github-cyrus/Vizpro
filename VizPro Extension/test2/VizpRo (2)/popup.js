
document.addEventListener('DOMContentLoaded', () => {
  chrome.runtime.sendMessage({ action: 'getTabTimes' }, response => {
    const tabTimes = response;
    const ul = document.getElementById('tabTimes');
    ul.innerHTML = '';
    for (const tabId in tabTimes) {
      const li = document.createElement('li');
      li.textContent = `Tab ${tabId}: ${Math.floor(tabTimes[tabId] / 1000)} seconds`;
      ul.appendChild(li);
    }
  });
});
