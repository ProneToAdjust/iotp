<!DOCTYPE html>
<html lang="en">
<head>
    <link rel= "stylesheet">
    <meta charset="UTF-8">
    <style>

    </style>
    <title>
        turnOnLED
    </title>
</head>
<body>
	
<div align = "center">
    <form action="turnOffLED.php" method="post">
        
        <input type="submit" value="On">
    </form>
</div>
	
<?php
	echo $result = shell_exec("python3 /var/www/html/setLED.py 'off'");
?>

</body>
</html>
