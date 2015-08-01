$(document).ready(function() {
  var href = window.location.href,
      url = href.split('?')[0],
      querystring = href.split('?')[1];

  $(".admin").on("click", ".more", function(event) {
    $.ajax({
      url: url + "page/" + $(event.target).data("page") + "/?" + querystring,
      dataType: "html",
      success: function(data) {
        // remove more button
        $(".admin .more").remove();

        // insert next page content
        $(".admin .links").append(data);
      },
      error: function(err) {
        // remove more button anyway
        $(".admin .more").remove();
      }
    });

    // don't submit the form
    event.preventDefault();
  });

  $(".admin").on("click", ".delete", function(event) {
    $.ajax({
      url: $(event.target).attr("href"),
      dataType: "json",
      success: function(data) {
        if (console) { console.log(data); }

        if (data.deleted) {
          // remove table row
          $("#short-" + data.short).remove();
        }
      }
    });

    // don't submit the form
    event.preventDefault();
  });
});
