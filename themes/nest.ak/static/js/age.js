//alert('hello');


function loadCatAge() {
    var elem = document.getElementById('juniper-age');
    var fitzElem = document.getElementById('fitz-age');

    var juniper = new Date('April 15, 2018 06:32:00');
    var juniperEomDays = 15;
    var juniperEoyMonths = 12 - 4;
    var fitz = new Date(2018, (6-1), 9, 22, 14, 0, 0);
    var fitzEomDays = 21;
    var fitzEoyMonths = 12 - 6;

    var currentDate = new Date(Date.now());

    var juniperAge = eachAge(currentDate, juniper, juniperEomDays, juniperEoyMonths);
    var fitzAge = eachAge(currentDate, fitz, fitzEomDays, fitzEoyMonths);

    elem.innerHTML = 'Juniper: ' + juniperAge;
    fitzElem.innerHTML = 'Fitz: ' + fitzAge;
}

function eachAge(currentDate, birthDate, restOfMonthDays, restOfYearMonths) {
    var ageYears = currentDate.getFullYear() - birthDate.getFullYear();
    var ageMonths = currentDate.getMonth() - birthDate.getMonth();
    var ageDays = currentDate.getDate() - birthDate.getDate();

    if (ageDays < 0) {
        ageMonths--;
        ageDays = currentDate.getDate() + restOfMonthDays;
    }

    if (ageMonths < 0) {
        ageYears--;
        ageMonths = currentDate.getMonth() + restOfYearMonths;
    }

    var ret = '';

    if (ageYears > 0) {
        ret += ageYears + ' years';
    }

    if (ageMonths > 0) {
        ret += ' ' + ageMonths + ' months';
    }

    if (ageDays > 0) {
        ret += ' ' + ageDays + ' days';
    }

    return ret;
}