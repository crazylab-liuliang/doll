<%--
  Created by IntelliJ IDEA.
  User: albert
  Date: 2017/12/18
  Time: 11:16
  To change this template use File | Settings | File Templates.
--%>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<html>
<head>
    <title>娃娃达人</title>
    <style type="text/css">
        html, body {
            background-color: #111;
            text-align: center;
        }
    </style>
</head>
<body>
    <canvas id="video-canvas"></canvas>
    <script type="text/javascript" src="dist/js/jsmpeg.min.js"></script>
    <script type="text/javascript">
        var canvas = document.getElementById('video-canvas');
        var url = 'ws://wawadaren.ledo.com:10002/camera_0';
        var player = new JSMpeg.Player(url, {canvas: canvas});
    </script>
</body>
</html>
