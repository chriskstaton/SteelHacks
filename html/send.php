<?php
    $title = $_POST["title"];
    $text = $_POST["text"];

    $db_user = "root";
    $db_pass = "letsmysql";
    $db_name = "music";

    $connection = mysql_connect("localhost", $db_user, $db_pass);
    mysql_select_db($db_name, $connection);

    $countQuery = "SELECT COUNT(*) FROM texts";
    $countResult = mysql_query($countQuery);

    $id = mysql_fetch_row($countResult)[0];

    $insertQuery = "INSERT INTO  texts (id, title, text) VALUES (0, '$title', '$text')";
    $insertResult = mysql_query($insertQuery);

    mysql_close($connection);


    $command = escapeshellcmd('python pythontest.py "'. $text . '"');
    $output = shell_exec($command);

?>