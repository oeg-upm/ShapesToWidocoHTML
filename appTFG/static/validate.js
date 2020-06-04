function validate(url,token){
    var checkbox= false;
    if ($('.inp').is(':checked')) {
        checkbox = true;
    }

    var dataValid = $('#textdata').val();
    dataValid = dataValid.replace(/\n/g, "\\n");
    var data = '{"coverage":' + checkbox + ', "dataValid": "' + dataValid + '"}'


    $.ajax({
            headers: { "X-CSRFToken": token },
            contentType: "application/json",
            type: 'POST',
            url: url,
            data: data,
            success:function(response) {
                if ($('#validationResponse').get().length != 0) {
                    $("#validationResponse").remove();
                }

                if ($('#spanResponse').get().length != 0) {
                    $("#divResponse").remove();
                }
                if (dataValid.length == 0) {
                    $("#divValid").append("<b id='validationResponse' style='color: blue'>Data must be introduced.</b>");
                }
                else {
                    response.data = response.data.replace(/>/g, "")
                    response.data = response.data.replace(/@/g, "\n@")
                    $("#divValid").append("<b id='validationResponse' style='color: blue'>Validation performed correctly.</b>");
                    $("#divValid").append("<div id='divResponse'> <b class='labelResponse'>Response:</b>" +
                        "<span id='spanResponse'>&nbsp;" + response.data.replace(/</g, "") + "</span></div>");
                }
            },
            error:function (response) {
                if ($('#validationResponse').get().length != 0) {
                    $("#validationResponse").remove();
                }
                if ($('#spanResponse').get().length != 0) {
                    $("#divResponse").remove();
                }
                $("#divValid").append("<b id='validationResponse' style='color: #CC0000'>Bad request.</b>");

                $("#divValid").append("<div id='divResponse'> <b class='labelResponse'>Error:</b>" +
                    " <span id='spanResponse'>&nbsp;" + response.responseJSON.data + "</span></div>");
            }
        });
}