// init copy to clipboard button
$(".copy-to-clipboard").on("click", function(event) {
  $('#' + $(event.target).data('copy-target')).select();

  try {
    var successful = document.execCommand('copy');
    var msg = successful ? 'successful' : 'unsuccessful';
    if (console) { console.log('Copying text command was ' + msg); }
  } catch(err) {
    if (console) { console.log('Oops, unable to cut'); }
  }

  // don't submit the form
  event.preventDefault();
});
