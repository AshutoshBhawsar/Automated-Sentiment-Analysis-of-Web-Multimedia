<html>
<body>

<?php

header("Access-Control-Allow-Origin: *");

$site=$_POST["url"];

if ($site == "") {
	echo "Got Empty URL!";
}
else if ($site == "undefined") {
	echo "Got Undefined URL!";
}
else {
	$bytes=file_put_contents('url.txt', $site);
	$bytes=file_put_contents('../Program/url.txt', $site);

	$output = exec('python ../Program/run_cmd_line.py 2>&1');
	echo $output;
}
?>
</body>
</html>