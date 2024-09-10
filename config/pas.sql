-- phpMyAdmin SQL Dump
-- version 5.2.1-4.fc40
-- https://www.phpmyadmin.net/
--
-- Servidor: localhost
-- Tiempo de generación: 01-09-2024 a las 21:26:19
-- Versión del servidor: 10.11.8-MariaDB
-- Versión de PHP: 8.3.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `pas`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `alarm_logs`
--

CREATE TABLE `alarm_logs` (
  `id` int(11) NOT NULL,
  `alarm_id` int(11) DEFAULT NULL,
  `action` varchar(255) DEFAULT NULL,
  `timestamp` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

--
-- Volcado de datos para la tabla `alarm_logs`
--

INSERT INTO `alarm_logs` (`id`, `alarm_id`, `action`, `timestamp`) VALUES
(293, 1, 'Alarma activada por interfaz web', '2024-08-01 17:57:10'),
(294, 1, 'Alarma desactivada por interfaz web', '2024-08-01 17:57:26'),
(295, 1, 'Alarma activada por None', '2024-09-01 15:41:06'),
(296, 1, 'Alarma desactivada por None', '2024-09-01 16:24:19'),
(297, 1, 'Alarma activada por None', '2024-09-01 16:24:24'),
(298, 1, 'Alarma desactivada por None', '2024-09-01 16:24:27'),
(299, 1, 'Alarma activada por None', '2024-09-01 16:26:15'),
(300, 1, 'Alarma desactivada por None', '2024-09-01 16:26:20'),
(301, 1, 'Alarma activada por None', '2024-09-01 16:26:51'),
(302, 1, 'Alarma desactivada por None', '2024-09-01 16:26:56'),
(303, 1, 'Alarma activada por None', '2024-09-01 16:30:25'),
(304, 1, 'Alarma desactivada por None', '2024-09-01 16:30:29'),
(305, 1, 'Alarma activada por None', '2024-09-01 16:31:06'),
(306, 1, 'Alarma desactivada por None', '2024-09-01 16:31:07'),
(307, 1, 'Alarma activada por None', '2024-09-01 16:31:11'),
(308, 1, 'Alarma desactivada por None', '2024-09-01 16:31:12'),
(309, 1, 'Alarma activada por interfaz web', '2024-09-01 16:31:39'),
(310, 1, 'Alarma desactivada por interfaz web', '2024-09-01 16:34:55');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `automation`
--

CREATE TABLE `automation` (
  `id` int(11) NOT NULL,
  `alarm_id` int(11) NOT NULL,
  `status` int(11) NOT NULL,
  `turnOnHour` time NOT NULL,
  `turnOffHour` time NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

--
-- Volcado de datos para la tabla `automation`
--

INSERT INTO `automation` (`id`, `alarm_id`, `status`, `turnOnHour`, `turnOffHour`) VALUES
(1, 1, 1, '18:00:00', '23:00:00');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `detection_logs`
--

CREATE TABLE `detection_logs` (
  `id` int(11) NOT NULL,
  `alarm_id` int(11) NOT NULL,
  `action` varchar(255) NOT NULL,
  `timestamp` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `detection_logs`
--

INSERT INTO `detection_logs` (`id`, `alarm_id`, `action`, `timestamp`) VALUES
(17, 1, 'Intruso detectado', '2024-09-01 16:37:18'),
(18, 1, 'Intruso detectado', '2024-09-01 16:38:04');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `devices`
--

CREATE TABLE `devices` (
  `id` int(11) NOT NULL,
  `name` varchar(44) NOT NULL,
  `status` int(11) NOT NULL,
  `activationPassword` varchar(220) NOT NULL,
  `rfid_status` int(11) NOT NULL,
  `rfid_temp` varchar(220) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

--
-- Volcado de datos para la tabla `devices`
--

INSERT INTO `devices` (`id`, `name`, `status`, `activationPassword`, `rfid_status`, `rfid_temp`) VALUES
(1, 'laser-alarm', 0, '12345', 0, 'saddsfdsfsdf');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `rfid`
--

CREATE TABLE `rfid` (
  `id` int(11) NOT NULL,
  `rfid_code` varchar(255) NOT NULL,
  `user_id` int(11) DEFAULT NULL,
  `device_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `rfid`
--

INSERT INTO `rfid` (`id`, `rfid_code`, `user_id`, `device_id`) VALUES
(1, 'RFID123456', NULL, 1),
(2, 'hghsdgh', NULL, 1),
(3, 'sdfsfdsfd', NULL, 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `users`
--

CREATE TABLE `users` (
  `id` int(11) NOT NULL,
  `username` varchar(40) NOT NULL,
  `password` varchar(40) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

--
-- Volcado de datos para la tabla `users`
--

INSERT INTO `users` (`id`, `username`, `password`) VALUES
(1, 'admin', 'admin'),
(6, 'Fernando', '0522'),
(7, 'LUS', '0522'),
(8, 'Luis', '0522');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `alarm_logs`
--
ALTER TABLE `alarm_logs`
  ADD PRIMARY KEY (`id`),
  ADD KEY `FK_alarm_logs_device_id` (`alarm_id`);

--
-- Indices de la tabla `automation`
--
ALTER TABLE `automation`
  ADD PRIMARY KEY (`id`),
  ADD KEY `FK_automation_device_id` (`alarm_id`);

--
-- Indices de la tabla `detection_logs`
--
ALTER TABLE `detection_logs`
  ADD PRIMARY KEY (`id`),
  ADD KEY `FK_detection_logs_device_id` (`alarm_id`);

--
-- Indices de la tabla `devices`
--
ALTER TABLE `devices`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `rfid`
--
ALTER TABLE `rfid`
  ADD PRIMARY KEY (`id`),
  ADD KEY `user_id` (`user_id`),
  ADD KEY `device_id` (`device_id`);

--
-- Indices de la tabla `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `alarm_logs`
--
ALTER TABLE `alarm_logs`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=311;

--
-- AUTO_INCREMENT de la tabla `detection_logs`
--
ALTER TABLE `detection_logs`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=19;

--
-- AUTO_INCREMENT de la tabla `rfid`
--
ALTER TABLE `rfid`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `users`
--
ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `alarm_logs`
--
ALTER TABLE `alarm_logs`
  ADD CONSTRAINT `FK_alarm_logs_device_id` FOREIGN KEY (`alarm_id`) REFERENCES `devices` (`id`);

--
-- Filtros para la tabla `automation`
--
ALTER TABLE `automation`
  ADD CONSTRAINT `FK_automation_device_id` FOREIGN KEY (`alarm_id`) REFERENCES `devices` (`id`);

--
-- Filtros para la tabla `detection_logs`
--
ALTER TABLE `detection_logs`
  ADD CONSTRAINT `FK_detection_logs_device_id` FOREIGN KEY (`alarm_id`) REFERENCES `devices` (`id`);

--
-- Filtros para la tabla `rfid`
--
ALTER TABLE `rfid`
  ADD CONSTRAINT `rfid_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE SET NULL,
  ADD CONSTRAINT `rfid_ibfk_2` FOREIGN KEY (`device_id`) REFERENCES `devices` (`id`) ON DELETE SET NULL;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
