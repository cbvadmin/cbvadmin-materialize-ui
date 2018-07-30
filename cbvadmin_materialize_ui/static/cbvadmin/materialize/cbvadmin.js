$(document).ready(function(){
    $('.modal').modal()
    $('.collapsible').collapsible();
    $('.left.sidenav').sidenav();
    $('.right.sidenav').sidenav({edge: 'right'})
    $('.fixed-action-btn').floatingActionButton();
    $('select').formSelect();
    $('.form-submit').click(function(e){
        target = $(this).attr("href")
        $(target).submit()
        return false
    })
    locale = moment()._locale._config
    $('.dateinput').datepicker({
        format: locale.longDateFormat['L'].toLowerCase(),
        parse: function(datetime) {
            return moment(datetime).format('L');
        },
        i18n: {
            months: locale.months,
            monthsShort: locale.monthsShort,
            weekdaysFull: locale.weekdays,
            weekdaysShort: locale.weekdaysShort,
            weekdaysAbbrev: locale.weekdaysMin
        }
    });
})
