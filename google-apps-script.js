// Google Apps Script code for FadiMind Echo cloud storage
// Deploy this as a web app with "Execute as: Me" and "Who has access: Anyone"

function doPost(e) {
  try {
    // Get the active spreadsheet and sheet
    const sheet = SpreadsheetApp.getActiveSpreadsheet().getSheetByName("Sheet1");
    
    // Extract parameters from the request
    const text = e.parameter.text;
    const timestamp = new Date();
    
    // Create a formatted timestamp in Arabic-friendly format
    const arabicTimestamp = Utilities.formatDate(timestamp, "GMT+3", "yyyy-MM-dd HH:mm:ss");
    
    // Append the data to the sheet
    sheet.appendRow([arabicTimestamp, text]);
    
    // Return success response in Arabic
    return ContentService
      .createTextOutput("تم الحفظ ✅")
      .setMimeType(ContentService.MimeType.TEXT);
      
  } catch (error) {
    // Return error response in Arabic
    return ContentService
      .createTextOutput("خطأ في الحفظ ❌: " + error.toString())
      .setMimeType(ContentService.MimeType.TEXT);
  }
}

// Optional: Function to initialize the spreadsheet with headers
function initializeSheet() {
  const sheet = SpreadsheetApp.getActiveSpreadsheet().getSheetByName("Sheet1");
  
  // Check if headers already exist
  if (sheet.getRange(1, 1).getValue() === "") {
    sheet.getRange(1, 1, 1, 2).setValues([["التاريخ والوقت", "النص المحفوظ"]]);
    sheet.getRange(1, 1, 1, 2).setFontWeight("bold");
  }
}