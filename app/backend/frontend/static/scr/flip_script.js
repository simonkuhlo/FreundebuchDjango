let current_page_index = 0

function attachButtonListeners(pageElement) {
    const nextBtn = pageElement.querySelector(".next-btn");
    if (nextBtn) {
      nextBtn.addEventListener("click", () => {
        next_page();
      });
    }
    const backBtn = pageElement.querySelector(".back-btn");
    if (backBtn) {
      backBtn.addEventListener("click", () => {
        prev_page();
      });
    }
}

function next_page() {

}

function prev_page() {

}

document.addEventListener("DOMContentLoaded", () => {
  const pageRoot = document.getElementById("page-root");
  let currentPage = 0;
  const pages = []; // Track loaded pages by index

  // Initialize with minimal pages loaded
  function initPages(initialCount = 2) {
    for (let i = 0; i < initialCount; i++) {
      loadPage(i);
    }
  }

  function loadPage(pageIndex) {
    if (pages.includes(pageIndex)) return; // Already loaded
    pages.push(pageIndex);
    pages.sort((a,b) => a-b);
    fetch(`/book/next_page/${pageIndex}`)
      .then(response => response.text())
      .then(html => {
        // Insert page HTML in the correct order by index
        // Pages assumed to have id="p{pageIndex}" for sorting and stacking
        const tempDiv = document.createElement("div");
        tempDiv.innerHTML = html;
        const newPage = tempDiv.firstElementChild;
        newPage.style.zIndex = pages.length - pages.indexOf(pageIndex);
        pageRoot.insertAdjacentElement("beforeend", newPage);
        attachButtonListeners(newPage, pageIndex);
      });
  }



  // Flip forward, then load next page if needed
  function flipPageForward(pageIndex) {
    const page = document.getElementById(`p${pageIndex}`);
    if (!page.classList.contains("flipped")) {
        console.log("flipping page")
      page.classList.add("flipped");
      currentPage = Math.max(currentPage, pageIndex + 1);
      // Load next page after this one
      loadPage(pageIndex + 1);
      updateZIndices();
    }
  }

  // Flip backward, then load previous page if needed
function flipPageBackward(pageIndex) {
  const page = document.getElementById(`p${pageIndex}`);
  if (page.classList.contains("flipped")) {
    page.classList.remove("flipped");
    currentPage = pageIndex - 1; // Update current page index correctly
    if (pageIndex > 0) loadPage(pageIndex - 1);
    updateZIndices();  // Recalculate z-index AFTER unflipping
  }
}

function updateZIndices() {
  const allPages = Array.from(pageRoot.querySelectorAll(".flip"));
  // For visible (not flipped) pages, assign ascending z-indices by page index
  let zIndexForVisible = 1;
  allPages
    .filter(p => !p.classList.contains("flipped"))
    .sort((a, b) => parseInt(a.id.replace("p", ""), 10) - parseInt(b.id.replace("p", ""), 10))
    .forEach(p => {
      p.style.zIndex = zIndexForVisible++;
    });

  // For flipped pages, assign descending z-indices by page index
  let zIndexForFlipped = allPages.length;
  allPages
    .filter(p => p.classList.contains("flipped"))
    .sort((a, b) => parseInt(b.id.replace("p", ""), 10) - parseInt(a.id.replace("p", ""), 10))
    .forEach(p => {
      p.style.zIndex = zIndexForFlipped--;
    });
}



  initPages(2); // Load initial pages
});

