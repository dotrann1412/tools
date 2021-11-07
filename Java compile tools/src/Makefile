MAKEFLAGS += --silent

DTO.class: DTO/*.java
	javac -cp . DTO/*.java -d .

GUI.class: GUI/*.java
	javac -cp . GUI/*.java -d .

run:
	java GUI/Tester.java

clean:
	rm -f -- /DTO/*.class /GUI/*.class 