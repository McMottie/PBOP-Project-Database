-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jan 14, 2024 at 01:03 PM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `5220411458`
--

-- --------------------------------------------------------

--
-- Table structure for table `menu`
--

CREATE TABLE `menu` (
  `id` int(11) NOT NULL,
  `makanan` varchar(100) NOT NULL,
  `karbohidrat` varchar(100) NOT NULL,
  `protein` varchar(100) NOT NULL,
  `lemak` varchar(100) NOT NULL,
  `kategori` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `menu`
--

INSERT INTO `menu` (`id`, `makanan`, `karbohidrat`, `protein`, `lemak`, `kategori`) VALUES
(902, 'Nasi Uduk', '1000', '1000', '100', 'breakfast'),
(903, 'Bubur Ayam', '36', '28', '12', 'breakfast'),
(904, 'Sandwich Daging', '26', '27', '13', 'breakfast'),
(905, 'Soto Ayam', '20', '24', '15', 'lunch'),
(906, 'Lontong Sayur', '59', '11', '8', 'lunch'),
(907, 'Gudeg', '18', '8', '11', 'lunch'),
(908, 'Mie Rebus', '40', '7', '3', 'dinner'),
(910, 'Mie Goreng', '40', '7', '3', 'dinner'),
(911, 'Nasi Goreng', '10000', '1000', '10', 'dinner'),
(918, 'Nasi Lemak', '100', '100', '100', 'dinner'),
(920, 'Nasi Kepal', '100', '100', '100', 'breakfast');

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE `user` (
  `id` int(11) NOT NULL,
  `username` varchar(100) NOT NULL,
  `password` varchar(100) NOT NULL,
  `tipe_akun` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`id`, `username`, `password`, `tipe_akun`) VALUES
(802, 'diki', 'dikidjvw', 11111),
(803, 'jati', 'jatidjvw', 11111),
(804, 'vincent', 'vincentdjvw', 22222),
(805, 'widan', 'widandjvw', 11111);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `menu`
--
ALTER TABLE `menu`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
