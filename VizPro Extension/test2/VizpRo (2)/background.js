
let activeTabId = null;
let startTime = null;
let tabTimes = {};

function updateTime() {
  if (activeTabId !== null && startTime !== null) {
    const now = Date.now();
    const elapsed = now - startTime;
    if (!tabTimes[activeTabId]) {
      tabTimes[activeTabId] = 0;
    }
    tabTimes[activeTabId] += elapsed;
    startTime = now;
  }
}

chrome.tabs.onActivated.addListener(activeInfo => {
  updateTime();
  activeTabId = activeInfo.tabId;
  startTime = Date.now();
});

chrome.tabs.onRemoved.addListener(tabId => {
  if (tabId === activeTabId) {
    updateTime();
    activeTabId = null;
    startTime = null;
  }
});

chrome.tabs.onUpdated.addListener((tabId, changeInfo, tab) => {
  if (tabId === activeTabId && changeInfo.status === "complete") {
    updateTime();
    startTime = Date.now();
  }
});

chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
  if (request.action === "getTabTimes") {
    updateTime();
    sendResponse(tabTimes);
  }
});
