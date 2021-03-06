from Id import Id
from Core import Core

class IdList:
	
	def parse(self, parser):
		self.id = Id()
		self.id.parse(parser)
		if parser.scanner.currentToken() == Core.COMMA:
			parser.scanner.nextToken()
			self.list = IdList()
			self.list.parse(parser)
	
	def print(self):
		self.id.print()
		if hasattr(self, 'list'):
			print(",", end='')
			self.list.print()
			
	# called by DeclInt.semantic
	def semanticIntVars(self, parser):
		self.id.doublyDeclared(parser)
		self.id.addToScopes(parser, Core.INT)
		if hasattr(self, 'list'):
			self.list.semanticIntVars(parser)

	# called by DeclClass.semantic
	def semanticRefVars(self, parser):
		self.id.doublyDeclared(parser)
		self.id.addToScopes(parser, Core.REF)
		if hasattr(self, 'list'):
			self.list.semanticRefVars(parser)

	def executeIntIdList(self, executor):
		self.id.executeIntAllocate(executor)
		if hasattr(self, 'list'):
			self.list.executeIntIdList(executor)

	def executeRefIdList(self, executor):
		self.id.executeRefAllocate(executor)
		if hasattr(self, 'list'):
			self.list.executeRefIdList(executor)