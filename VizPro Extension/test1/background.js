let activeTabId = null;
let activeStartTime = null;
const tabTimes = {};

chrome.tabs.onActivated.addListener(activeInfo => {
  if (activeTabId !== null && activeStartTime !== null) {
    const elapsedTime = Date.now() - activeStartTime;
    if (!tabTimes[activeTabId]) {
      tabTimes[activeTabId] = 0;
    }
    tabTimes[activeTabId] += elapsedTime;
  }

  activeTabId = activeInfo.tabId;
  activeStartTime = Date.now();
});

chrome.tabs.onRemoved.addListener(tabId => {
  if (tabId === activeTabId && activeStartTime !== null) {
    const elapsedTime = Date.now() - activeStartTime;
    if (!tabTimes[tabId]) {
      tabTimes[tabId] = 0;
    }
    tabTimes[tabId] += elapsedTime;
    activeTabId = null;
    activeStartTime = null;
  }
  delete tabTimes[tabId];
});

chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
  if (message.type === 'getTabTimes') {
    sendResponse(tabTimes);
  }
});