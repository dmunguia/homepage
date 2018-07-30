interface Circuit {
	boolean eval()
}

class AND implements Circuit {
	Circuit[] inputs

	boolean eval() {
		boolean value = true
		for (input in inputs) {
			value = value && input.eval()
		}

		return value
	}
}

class OR implements Circuit {
	Circuit[] inputs

	boolean eval() {
		boolean value = false
		for (input in inputs) {
			value = value || input.eval()
		}

		return value
	}
}

class NOT implements Circuit {
	Circuit input

	boolean eval() {
		return !input.eval()
	}
}

class Input implements Circuit {
	boolean value

	boolean eval() {
		return value
	}
}

def verifyCSAT(Circuit circuit) {
	return circuit.eval()
}

def x1 = new Input(value: true)
def x2 = new Input(value: true)
def x3 = new Input(value: false)

Circuit circuit = 
	new AND(inputs: [
		new OR(inputs: [
			new OR(inputs: [x1, x2]), 
			new NOT(input: 
				new NOT(input: x3)
			)
		]),
		new OR(inputs: [
			new NOT(input:
				new NOT(input: x3)
			),
			new AND(inputs: [
				x1,
				new NOT(input: x3),
				x2
			])
		]),
		new AND(inputs: [
			x1,
			new NOT(input: x3),
			x2
		])
	])

verifyCSAT(circuit)