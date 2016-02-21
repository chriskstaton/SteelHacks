<?php

    $db_user = "root";
    $db_pass = "letsmysql";
    $db_name = "music";

    $connection = mysql_connect("localhost", $db_user, $db_pass);
    mysql_select_db($db_name, $connection);

    $selectQuery = "SELECT * FROM texts";
    $selectResult = mysql_query($selectQuery);

    mysql_close($connection);


    $rows = mysql_num_rows($selectResult);

    $array[] = array();
    $array["length"] = $rows;


    for($i = 0; $i < $rows; $i++)
    {
        $row = mysql_fetch_row($selectResult);
        $array[$i] = $row[1];
    }

    echo(json_encode($array))

?>