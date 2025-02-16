
function updateCSS(tags, addClasses = [], removeClasses = []) {
    tags.forEach(tag => {
        document.querySelectorAll(tag).forEach(element => {
            removeClasses.forEach(cls => element.classList.remove(cls));
            addClasses.forEach(cls => element.classList.add(cls));
        });
    });
}



updateCSS(['h1'], ['text-3xl', 'font-bold']);
updateCSS(['h2'], ['text-xl', 'font-semibold', 'mt-8']);
updateCSS(['h3'], ['font-semibold', 'mb-5']);
updateCSS(['h4'], ['font-semibold', 'mt-4']);
updateCSS(['p'], ['mt-1', 'text-md', 'text-muted-foreground', "text-justify"]);
updateCSS(['ul'], ['list-disc', 'pl-10']);
updateCSS(['li'], ['m-0', 'p-0']);
updateCSS(['table'], ['table', 'table-sm', 'mb-4']);
updateCSS(['img'], ["p-10"]);
updateCSS(['a'], ['text-blue-700', "underline"]);
// updateTailwindDaisyUI(['h2'], ['text-xl', 'mt-4']);
// updateTailwindDaisyUI(['h2'], ['text-xl', 'mt-4']);
// updateTailwindDaisyUI(['h2'], ['text-xl', 'mt-4']);
// updateTailwindDaisyUI(['h2'], ['text-xl', 'mt-4']);
// updateTailwindDaisyUI(['h2'], ['text-xl', 'mt-4']);

document.querySelector("main").className = "container mx-auto px-4 py-8 overflow-y-scroll print:px-0"
generateIndex();
document.body.classList.add("flex", "print:block", "h-screen", "text-sm")