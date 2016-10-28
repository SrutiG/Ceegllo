
$(document).ready(function() {
    $("#cancelBT").click(function() {
        parent.history.back();
        return false;
    });

});

function editCollege(){
        window.location="../editcollege";
    }

function goBack() {
    window.history.back();
}

