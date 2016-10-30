
$(document).ready(function() {
    $("#cancelBT").click(function() {
        parent.history.back();
        return false;
    });
    $(".dropdown-toggle").dropdown();


});

function editCollege(){
        window.location="../editcollege";
    }

function goBack() {
    window.history.back();
}

