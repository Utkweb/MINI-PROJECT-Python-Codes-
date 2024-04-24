const fs = require('fs');
const XLSX = require('xlsx');


function processJSON(jsonData) {
    const workbook = XLSX.utils.book_new();

    
    const mainDataSheet = XLSX.utils.json_to_sheet([jsonData]);
    XLSX.utils.book_append_sheet(workbook, mainDataSheet, 'MainData');

    
    jsonData.sections.forEach((section, index) => {
        const sheetName = `Section_${index + 1}`;
        const sectionSheet = XLSX.utils.json_to_sheet(section.books);
        XLSX.utils.book_append_sheet(workbook, sectionSheet, sheetName);
    });

    XLSX.writeFile(workbook, 'output.xlsx');
}

try {
    
    const jsonString = fs.readFileSync('sample.json', 'utf8');
    const jsonData = JSON.parse(jsonString);

    
    processJSON(jsonData);

    console.log('Conversion successful! Check the output.xlsx file.');
} catch (error) {
    console.error('Error:', error.message);
}
