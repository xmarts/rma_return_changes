# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError


class ValidationRma_n(models.Model):

	_inherit = 'stock.picking'


class ValidationR(models.Model):

	_inherit ='crm.claim.ept'


	purchase_id = fields.Many2one('purchase.order', string="Purcharse_id", compute="onchange_picking_id_add")


	state = fields.Selection([('draft','Draft'),('approve','Approved'),('review','Review piece'),('state','good condition'),('default','manufacturing'),('process','Processing'),('close','Closed'),('reject','Rejected')])



	@api.onchange('picking_id')
	def onchange_picking_id_add(self):
		if self.picking_id:
			valor = self.picking_id.purchase_id.id
			self.purchase_id = valor
	

	@api.one
	def reviewpiezza(self):
		self.write({'state':'review'})

	@api.one
	def statecondition(self):
		self.write({'state':'state'})

	@api.one
	def defaultmanu(self):
		self.write({'state':'default'})

	
	@api.one
	def processva(self):
		self.write({'state':'process'})	


	@api.one
	def manufacturingproc(self):
		self.write({'state':'process'})				
		








		





