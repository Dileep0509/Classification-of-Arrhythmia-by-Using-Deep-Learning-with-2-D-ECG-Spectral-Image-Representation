$(document).ready(function () {

    // Hide elements initially
    $('.image-section').hide();
    $('.loader').hide();
    $('#result').hide();

    // Image Preview Function
    function readURL(input) {

        if (input.files && input.files[0]) {

            let reader = new FileReader();

            reader.onload = function (e) {

                $('#imagePreview')
                    .css('background-image', 'url(' + e.target.result + ')')
                    .hide()
                    .fadeIn(650);

            };

            reader.readAsDataURL(input.files[0]);
        }
    }

    // File Upload Change Event
    $("#imageUpload").change(function () {

        $('.image-section').show();
        $('#btn-predict').show();

        $('#result').text('');
        $('#result').hide();

        readURL(this);

    });

    // Predict Button Click
    $('#btn-predict').click(function () {

        let form_data = new FormData($('#upload-file')[0]);

        // Hide button
        $(this).hide();

        // Show loader
        $('.loader').show();

        // AJAX request
        $.ajax({

            type: 'POST',
            url: '/predict',

            data: form_data,

            contentType: false,
            cache: false,
            processData: false,

            success: function (data) {

                // Hide loader
                $('.loader').hide();

                // Show result
                $('#result')
                    .fadeIn(600)
                    .html('<strong>Result:</strong> ' + data);

                console.log("Success:", data);

                // Show button again
                $('#btn-predict').show();
            },

            error: function (xhr, status, error) {

                $('.loader').hide();

                $('#result')
                    .fadeIn(600)
                    .html('<strong>Error:</strong> Prediction failed');

                console.error("Error:", error);

                $('#btn-predict').show();
            }

        });

    });

});