/**
 * Created by Aken on 2017/1/11.
 */
var page = require('webpage').create();
page.open("http://www.cnblogs.com/front-Thinking/", function(status) {
    if ( status === "success" ) {
        page.render("before.png");
        page.includeJs("http://code.jquery.com/jquery-1.10.1.min.js",
            function() {
                page.evaluate(function() {
                $('#Header1_HeaderTitle').html('My PhantomJS');
            });
            page.render("after.png");
            phantom.exit();();
        });
    }
});