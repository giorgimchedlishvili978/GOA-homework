(non-void)
function convertMinutesToSeconds(minutes) {
    return minutes * 60;
}
(non-void)
function sumAndMultiply(first, second, third) {
    return (first + second) * third;
}
True ან False (non-void)
function isFirstGreaterThanSecond(first, second) {
    return first > second;
}
(void)
function logElement(element) {
    console.log("Element: " + element);
}(void)
function setElementTextById(elementId, text) {
    const element = document.getElementById(elementId);
    if (element) {
        element.textContent = text;
    }
}
