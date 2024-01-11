$(document).ready(function() {
    const baseUrl = 'https://www.fourtonfish.com/hellosalut/hello/';

    $('#btn_translate').click(fetchTranslation);
    $('#language_code').keypress(function(event) {
        if (event.which === 13) {
            fetchTranslation();
        }
    });

    function fetchTranslation() {
        const languageCode = $('#language_code').val();
        const url = baseUrl + '?' + $.param({ lang: languageCode });

        $.get(url, function(data) {
            $('#hello').text(data.hello);
        });
    }
});
