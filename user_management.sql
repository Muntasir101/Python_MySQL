-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Nov 15, 2023 at 06:36 PM
-- Server version: 10.4.28-MariaDB
-- PHP Version: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `user_management`
--

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `id` int(11) NOT NULL,
  `name` varchar(100) NOT NULL,
  `email` varchar(255) NOT NULL,
  `password` varchar(50) NOT NULL,
  `address` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`id`, `name`, `email`, `password`, `address`) VALUES
(1, 'Mr.Smith', 'smith@gmail.com', '123456', 'Dhaka'),
(2, 'Kevin', 'mporcher0@reddit.com', 'yJ7#5JX4MY', 'Paris'),
(3, 'Green', 'hcasaccia1@bandcamp.com', 'xA7(K=zMt', 'paris'),
(4, 'Derwin Hawney', 'dhawney2@npr.org', 'bB4|nTu$zHS', '707 Fordem Circle'),
(5, 'Gianni Edeson', 'gedeson3@google.co.uk', 'qZ3~<1Et)T', 'NY'),
(7, 'Bridie Sherbrook', 'bsherbrook5@eepurl.com', 'nQ1&&`3vU~o&dtHc', 'NY'),
(8, 'Hoyt Konerding', 'hkonerding6@disqus.com', 'bG0.#$3bXbIr', '863 Havey Place'),
(9, 'Trevar Sonner', 'tsonner7@fda.gov', 'lU3{3.`ZC5', '512 Claremont Trail'),
(10, 'Giuditta Abramamov', 'gabramamov8@hp.com', 'vH0>?\"*Y03q6Z\')Z', '2 Harbort Road'),
(12, 'superman2', 'superman2@mail.com', '', NULL);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
