const test = require('node:test');
const assert = require('assert');
const { MyClass, Student } = require('./main');

test("Test MyClass's addStudent", () => {
    const myClass = new MyClass();
    const student = new Student();
    const newStudentId = myClass.addStudent(student);
    assert.strictEqual(newStudentId, 0);

    const badStudentId = myClass.addStudent("what");
    assert.strictEqual(badStudentId, -1);
});

test("Test MyClass's getStudentById", () => {
    const myClass = new MyClass();
    const student = new Student();
    myClass.addStudent(student);
    const studentById = myClass.getStudentById(0);
    assert.strictEqual(studentById, student);

    const badStudentById = myClass.getStudentById(-1);
    assert.strictEqual(badStudentById, null);


    const badStudentById2 = myClass.getStudentById(100);
    assert.strictEqual(badStudentById2, null);
});

test("Test Student's setName", () => {
    const student = new Student();
    student.setName('jjmow');
    assert.strictEqual(student.getName(), 'jjmow');

    student.setName(88);
    assert.strictEqual(student.getName(), 'jjmow');
});

test("Test Student's getName", () => {
    const student = new Student();
    student.setName('jjmow');
    assert.strictEqual(student.getName(), 'jjmow');
    
    const student2 = new Student();
    assert.strictEqual(student2.getName(), '');

});
