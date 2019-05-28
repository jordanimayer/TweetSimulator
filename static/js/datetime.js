/* Convert month number (0-11) to string */
function month_num2str(month_num) {
  var month_str = "";
  switch (month_num) {
    case 0:
      month_str = "January";
      break;
    case 1:
      month_str = "February";
      break;
    case 2:
      month_str = "March";
      break;
    case 3:
      month_str = "April";
      break;
    case 4:
      month_str = "May";
      break;
    case 5:
      month_str = "June";
      break;
    case 6:
      month_str = "July";
      break;
    case 7:
      month_str = "August";
      break;
    case 8:
      month_str = "September";
      break;
    case 9:
      month_str = "October";
      break;
    case 10:
      month_str = "November";
      break;
    case 11:
      month_str = "December";
      break;
    default:
      month_str = "This shouldn't happen";
  }

  return month_str;
}

/* Convert hour (0-23), minute (0-59), to time string with AM/PM */
function time_num2str(hour, minute) {
  var am_pm = "AM";
  if (hour == 0) {
    hour = 12;
  }
  if (hour > 12) {
    hour = hour - 12;
    am_pm = "PM";
  }
  hour_str = hour.toString();

  min_str = minute.toString();
  if (minute < 10) {
    min_str = "0" + min_str;
  }

  return (hour_str + ":" + min_str + " " + am_pm);
}

var current_dt = new Date();
var date = current_dt.getDate();
var month = current_dt.getMonth();
var year = current_dt.getFullYear();
var hour = current_dt.getHours();
var minute = current_dt.getMinutes();

var current_dt_str = time_num2str(hour, minute) + " - " + month_num2str(month) + " " + date + ", " + year;

document.getElementById("current-datetime").innerHTML = current_dt_str;
