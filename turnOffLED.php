<!DOCTYPE html>
<html lang="en">
<head>
    <link rel= "stylesheet">
    <meta charset="UTF-8">
    <style>

    </style>
    <title>
        turnOffLED
    </title>
</head>
<body>
	
<?php
	echo $result = shell_exec("python3 /var/www/html/setLED.py > /dev/null 2>/dev/null & 'on'");
?>

<div align = "center">
    <form action="turnOnLED.php" method="post">
        
        <input type="submit" value="Off">
    </form>
</div>
</body>
</html>
