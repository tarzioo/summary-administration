
function caseSearch(evt) {
    alert("Entered function");
    evt.preventDefault();

    var textInput = {
        "case_number": $("#case-search-field").val()
    };

    $.post("/case-search", textInput);
         
    
    //reloads the page after the ajax call
    //window.location.reload();
}

    $("#button-case-search").on("click", caseSearch);

