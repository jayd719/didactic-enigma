function generateIndex(containerId = "index") {
    const headings = document.querySelectorAll("h2,h3, h4, h5, h6");
    if (!headings.length) {
        console.warn("No headings found in the document.");
        return;
    }

    let container = document.getElementById(containerId);
    if (!container) {
        container = document.createElement("div");
        container.id = containerId;
        document.body.insertBefore(container, document.body.firstChild);
    }
    container.innerHTML = `<h3 style='margin-top:15px;'>Table of Contents</h3>`;

    const indexList = document.createElement("ul");
    indexList.className = "menu"
    container.appendChild(indexList);

    headings.forEach(heading => {
        const level = parseInt(heading.tagName[1]);
        const listItem = document.createElement("li");

        if (!heading.id) {
            heading.id = `91oz.-${Math.random().toString(36).substr(2, 9)}`;
        }
        const link = document.createElement("a");
        link.href = `#${heading.id}`;
        link.className = "m-0 p-0"
        link.textContent = heading.textContent;
        listItem.appendChild(link);
        listItem.style.marginLeft = `${(level - 1) * 15}px`;
        if (level == 2) {
            listItem.style.marginTop = "10px"
            listItem.style.fontWeight = 'bold'
        }

        indexList.appendChild(listItem);
    });
    container.classList.add("lg:w-96", "overflow-y-scroll", "pl-2", "border", "print:border-0")
}


function updateCSS(tags, addClasses = [], removeClasses = []) {
    tags.forEach(tag => {
        document.querySelectorAll(tag).forEach(element => {
            removeClasses.forEach(cls => element.classList.remove(cls));
            addClasses.forEach(cls => element.classList.add(cls));
        });
    });
}

function loadScript(src) {
    if (!document.querySelector(`script[src="${src}"]`)) {
        let script = document.createElement("script");
        script.src = src;
        script.onerror = () => console.error(`Failed to load script: ${src}`);
        document.head.appendChild(script);
    } else {
        console.log(`Script already loaded: ${src}`);
    }
}

// Function to dynamically load a stylesheet
function loadStylesheet(href) {
    if (!document.querySelector(`link[href="${href}"]`)) {
        let link = document.createElement("link");
        link.rel = "stylesheet";
        link.href = href;
        document.head.appendChild(link);
        console.log(`Stylesheet loaded: ${href}`);
    } else {
        console.log(`Stylesheet already loaded: ${href}`);
    }
}


loadScript("https://cdn.tailwindcss.com")
loadStylesheet("https://cdn.jsdelivr.net/npm/daisyui@4.12.23/dist/full.min.css");
document.documentElement.setAttribute("data-theme", "light");
setTimeout(() => {
    updateCSS(['h1'], ["text-5xl", "font-bold", "text-primary", "p-4", "border-b-4", "border-primary", "mb-8"]);
    updateCSS(['h2'], ["text-2xl", "font-semibold", "text-secondary", "p-3", "border-b-2", "border-secondary", "mt-10", "mb-2"]);
    updateCSS(['h3'], ["text-lg", "font-medium", "text-accent", "p-2", "border-b", "border-accent"]);
    updateCSS(['h4'], ["text-lg", "font-normal", "text-neutral", "p-1", "border-b", "border-neutral"]);
    updateCSS(['p'], ["text-base", "text-gray-700", "leading-relaxed", "mb-4"]);
    updateCSS(['ul'], ["list-disc", "list-inside", "text-gray-800", "space-y-2", "pl-4"]);
    updateCSS(['li'], ["text-base", "text-gray-700", "leading-normal"]);
    updateCSS(['table'], ["table", 'table-zebra', "w-full"]);
    updateCSS(["thead"], ["bg-base-300", "border", "border-2"])
    updateCSS(['img'], ["max-w-full", "h-auto", "p-6"]);
    updateCSS(['a'], ["text-blue-600", "hover:text-blue-800", "underline", "font-medium", "transition", "duration-200"]);
    document.querySelector("main").className = "container mx-auto px-4 py-8 overflow-y-scroll print:px-0"
    document.body.classList.add("lg:flex", "print:block", "h-screen", "text-sm")
    generateIndex();
}, 50);
document.documentElement.setAttribute("data-theme", "garden");
