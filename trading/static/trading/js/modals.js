import $ from 'jquery';

function open_modal(url) {
  $('#popup').load(url, function () {
    $(this).modal('show');
  });
  return false;
}