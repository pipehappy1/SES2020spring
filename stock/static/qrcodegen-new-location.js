"use strict";
var app;
(function (app) {
    let outputElem = document.getElementById("qrcode-place-holder");
    function initialize() {
        //getElem("loading").style.display = "none";
        //getElem("loaded").style.removeProperty("display");
        //let elems = document.querySelectorAll("input[type=number], textarea");
        //for (let el of elems) {
        //    if (el.id.indexOf("version-") != 0)
        //        el.oninput = redrawQrCode;
        //}
        //elems = document.querySelectorAll("input[type=radio], input[type=checkbox]");
        //for (let el of elems)
        //    el.onchange = redrawQrCode;
        redrawQrCode();
    }
    function redrawQrCode() {
	const incoming_id = "p-" + getElem("qrid").innerHTML;
	console.log("init qr code generating" + incoming_id);

	if (!incoming_id) {
	    console.log("There is no incoming id.")
	    return;
	}

	let outputElem = document.getElementById("qrcode-place-holder");
        const errCorLvl = qrcodegen.QrCode.Ecc.HIGH; // Error correction level
        const qr = qrcodegen.QrCode.encodeText(incoming_id, errCorLvl); // Make the QR Code symbol
        qr.drawCanvas(10, 4, appendCanvas("hello-world-QR")); // Draw it on screen
        // Show/hide rows based on bitmap/vector image output
        //const bitmapOutput = getInput("output-format-bitmap").checked;
        //const scaleRow = getElem("scale-row");
        //const svgXmlRow = getElem("svg-xml-row");
        //if (bitmapOutput) {
        //    scaleRow.style.removeProperty("display");
        //    svgXmlRow.style.display = "none";
        //}
        //else {
        //    scaleRow.style.display = "none";
        //    svgXmlRow.style.removeProperty("display");
        //}
        //const svgXml = getElem("svg-xml-output");
        //svgXml.value = "";
        //// Reset output images in case of early termination
        //const canvas = getElem("qrcode-canvas");
        //const svg = document.getElementById("qrcode-svg");
        //canvas.style.display = "none";
        //svg.style.display = "none";
        //// Returns a QrCode.Ecc object based on the radio buttons in the HTML form.
        //function getInputErrorCorrectionLevel() {
        //    if (getInput("errcorlvl-medium").checked)
        //        return qrcodegen.QrCode.Ecc.MEDIUM;
        //    else if (getInput("errcorlvl-quartile").checked)
        //        return qrcodegen.QrCode.Ecc.QUARTILE;
        //    else if (getInput("errcorlvl-high").checked)
        //        return qrcodegen.QrCode.Ecc.HIGH;
        //    else // In case no radio button is depressed
        //        return qrcodegen.QrCode.Ecc.LOW;
        //}
        //// Get form inputs and compute QR Code
        //const ecl = getInputErrorCorrectionLevel();
        //const text = getElem("text-input").value;
        //const segs = qrcodegen.QrSegment.makeSegments(text);
        //const minVer = parseInt(getInput("version-min-input").value, 10);
        //const maxVer = parseInt(getInput("version-max-input").value, 10);
        //const mask = parseInt(getInput("mask-input").value, 10);
        //const boostEcc = getInput("boost-ecc-input").checked;
        //const qr = qrcodegen.QrCode.encodeSegments(segs, ecl, minVer, maxVer, mask, boostEcc);
        //// Draw image output
        //const border = parseInt(getInput("border-input").value, 10);
        //if (border < 0 || border > 100)
        //    return;
        //if (bitmapOutput) {
        //    const scale = parseInt(getInput("scale-input").value, 10);
        //    if (scale <= 0 || scale > 30)
        //        return;
        //    qr.drawCanvas(scale, border, canvas);
        //    canvas.style.removeProperty("display");
        //}
        //else {
        //    const code = qr.toSvgString(border);
        //    const viewBox = / viewBox="([^"]*)"/.exec(code)[1];
        //    const pathD = / d="([^"]*)"/.exec(code)[1];
        //    svg.setAttribute("viewBox", viewBox);
        //    svg.querySelector("path").setAttribute("d", pathD);
        //    svg.style.removeProperty("display");
        //    svgXml.value = qr.toSvgString(border);
        //}
        //// Returns a string to describe the given list of segments.
        //function describeSegments(segs) {
        //    if (segs.length == 0)
        //        return "none";
        //    else if (segs.length == 1) {
        //        const mode = segs[0].mode;
        //        const Mode = qrcodegen.QrSegment.Mode;
        //        if (mode == Mode.NUMERIC)
        //            return "numeric";
        //        if (mode == Mode.ALPHANUMERIC)
        //            return "alphanumeric";
        //        if (mode == Mode.BYTE)
        //            return "byte";
        //        if (mode == Mode.KANJI)
        //            return "kanji";
        //        return "unknown";
        //    }
        //    else
        //        return "multiple";
        //}
        //// Returns the number of Unicode code points in the given UTF-16 string.
        //function countUnicodeChars(str) {
        //    let result = 0;
        //    for (let i = 0; i < str.length; i++, result++) {
        //        const c = str.charCodeAt(i);
        //        if (c < 0xD800 || c >= 0xE000)
        //            continue;
        //        else if (0xD800 <= c && c < 0xDC00 && i + 1 < str.length) { // High surrogate
        //            i++;
        //            const d = str.charCodeAt(i);
        //            if (0xDC00 <= d && d < 0xE000) // Low surrogate
        //                continue;
        //        }
        //        throw "Invalid UTF-16 string";
        //    }
        //    return result;
        //}
        //// Show the QR Code symbol's statistics as a string
        //getElem("statistics-output").textContent = `QR Code version = ${qr.version}, ` +
        //    `mask pattern = ${qr.mask}, ` +
        //    `character count = ${countUnicodeChars(text)},\n` +
        //    `encoding mode = ${describeSegments(segs)}, ` +
        //    `error correction = level ${"LMQH".charAt(qr.errorCorrectionLevel.ordinal)}, ` +
        //    `data bits = ${qrcodegen.QrSegment.getTotalBits(segs, qr.version)}.`;
    }
    function handleVersionMinMax(which) {
        const minElem = getInput("version-min-input");
        const maxElem = getInput("version-max-input");
        let minVal = parseInt(minElem.value, 10);
        let maxVal = parseInt(maxElem.value, 10);
        minVal = Math.max(Math.min(minVal, qrcodegen.QrCode.MAX_VERSION), qrcodegen.QrCode.MIN_VERSION);
        maxVal = Math.max(Math.min(maxVal, qrcodegen.QrCode.MAX_VERSION), qrcodegen.QrCode.MIN_VERSION);
        if (which == "min" && minVal > maxVal)
            maxVal = minVal;
        else if (which == "max" && maxVal < minVal)
            minVal = maxVal;
        minElem.value = minVal.toString();
        maxElem.value = maxVal.toString();
        redrawQrCode();
    }
    app.handleVersionMinMax = handleVersionMinMax;
    function getElem(id) {
        const result = document.getElementById(id);
        if (result instanceof HTMLElement)
            return result;
        throw "Assertion error";
    }
    function getInput(id) {
        const result = getElem(id);
        if (result instanceof HTMLInputElement)
            return result;
        throw "Assertion error";
    }
    function appendCanvas(caption) {
        //let p = outputElem.appendChild(document.createElement("p"));
        //p.textContent = caption + ":";
        let result = document.createElement("canvas");
        outputElem.appendChild(result);
        return result;
    }
    initialize();
})(app || (app = {}));
