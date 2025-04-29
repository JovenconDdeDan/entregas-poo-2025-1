INSERT INTO `pdbs2`.`usuarios` (`id`, `nombre`, `email`, `contraseña`) VALUES ('1', 'Juan Camilo Arjona Valderrama', 'carjona374tr@hotmail.com', '37yrbfu8349u++');
INSERT INTO `pdbs2`.`usuarios` (`id`, `nombre`, `email`, `contraseña`) VALUES ('2', 'Andrea Pastrana Sierra', 'aps2020org@outlook.com', '74nbdlsoiucr8');
INSERT INTO `pdbs2`.`usuarios` (`id`, `nombre`, `email`, `contraseña`) VALUES ('3', 'Simón Pedro Carranza Lopez', 'setenta364si@gmail.com', 'maquinaarbol999');

INSERT INTO `pdbs2`.`productos` (`id`, `nombre`, `descripcion`, `precio`, `stock`) VALUES ('1', 'leche entera', 'leche de vaca entera pasteurizada ( 1L )', '6000', '70');
INSERT INTO `pdbs2`.`productos` (`id`, `nombre`, `descripcion`, `precio`, `stock`) VALUES ('2', 'nuez moscada', 'nuez moscada molida especia aromática ( 500gr )', '30000', '50');
INSERT INTO `pdbs2`.`productos` (`id`, `nombre`, `descripcion`, `precio`, `stock`) VALUES ('3', 'lonja de bocadilo', 'lonja de guayaba ( 300gr )', '2150', '235');

INSERT INTO `pdbs2`.`carrito` (`id`, `usuario_id`, `producto_id`, `cantidad`) VALUES ('1', '2', '1', '4');
INSERT INTO `pdbs2`.`carrito` (`id`, `usuario_id`, `producto_id`, `cantidad`) VALUES ('2', '2', '2', '1');
INSERT INTO `pdbs2`.`carrito` (`id`, `usuario_id`, `producto_id`, `cantidad`) VALUES ('3', '3', '3', '10');

INSERT INTO `pdbs2`.`pedidos` (`id`, `usuario_id`, `total_precio`, `estado_p`) VALUES ('1', '2', '24000', 'pendiente');
INSERT INTO `pdbs2`.`pedidos` (`id`, `usuario_id`, `total_precio`, `estado_p`) VALUES ('2', '2', '30000', 'cancelado');
INSERT INTO `pdbs2`.`pedidos` (`id`, `usuario_id`, `total_precio`, `estado_p`) VALUES ('3', '3', '21500', 'pagado');

INSERT INTO `pdbs2`.`pedido_detalle` (`id`, `pedido_id`, `producto_id`, `cantidad`, `precio_unitario`) VALUES ('1', '1', '1', '4', '6000');
INSERT INTO `pdbs2`.`pedido_detalle` (`id`, `pedido_id`, `producto_id`, `cantidad`, `precio_unitario`) VALUES ('2', '2', '2', '1', '30000');
INSERT INTO `pdbs2`.`pedido_detalle` (`id`, `pedido_id`, `producto_id`, `cantidad`, `precio_unitario`) VALUES ('3', '3', '3', '10', '2150');

INSERT INTO `pdbs2`.`pagos` (`id`, `pedido_id`, `metodo_pago`, `estado_pago`, `referencia_pago`) VALUES ('1', '1', 'T. Débito', 'exitoso', '3452');
INSERT INTO `pdbs2`.`pagos` (`id`, `pedido_id`, `metodo_pago`, `estado_pago`, `referencia_pago`) VALUES ('2', '2', 'T. crédito', 'exitoso', '3466');
INSERT INTO `pdbs2`.`pagos` (`id`, `pedido_id`, `metodo_pago`, `estado_pago`, `referencia_pago`) VALUES ('3', '3', 'Efectivo', 'fallido', '2380');
