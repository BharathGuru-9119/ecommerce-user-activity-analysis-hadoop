document.addEventListener('DOMContentLoaded', () => {

  // track when user enters the site
  const sessionStart = Date.now();

  // helper for sending logs
  function logEvent(action, extra = {}) {
    fetch("/log", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        action,
        timestamp: new Date().toISOString(),
        ...extra
      })
    }).catch(err => console.error("Log error:", err));
  }

  // basic click logs
  document.body.addEventListener('click', e => {
    let action = e.target.innerText.trim() || e.target.alt || e.target.className || "Unknown";
    logEvent(`Clicked: ${action}`);
  });

  // screen-time logging before unload
  window.addEventListener('beforeunload', () => {
    const timeSpent = ((Date.now() - sessionStart) / 1000).toFixed(2); // in seconds
    logEvent("Session Ended", { time_spent_seconds: timeSpent });
  });

  // also log session start
  logEvent("Session Started");
});
