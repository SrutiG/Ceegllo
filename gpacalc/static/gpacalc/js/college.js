function College(semesters, name) {
    this.name = name;
    this.semesters = semesters;
    this.gpaCalc = new calculateGPA(semesters);
    this.gpa = this.gpaCalc.gpa;
}

function Semester(classes, season, year) {
    this.classes = classes;
    this.season = season;
    this.year = year;

    this.toString = function() {
        return this.season + " " + this.year;
    }
}

function pastSemester(classes, season, year) {
    Semester.call(this, classes, season, year);
    this.gpaCalc = new calculateGPA(classes);
    this.gpa = this.gpaCalc.gpa;
    this.credits = this.gpaCalc.total;
}

pastSemester.prototype = Semester.prototype;
pastSemester.prototype.constructor = pastSemester;

function Class(name, credits) {
    this.name = name;
    this.credits = credits;
    this.toString = function() {
        return this.name + " " + this.credits;
    }
}

function pastClass(name, credits, gpa) {
    Class.call(this, name, credits);
    this.gpa = gpa;
    this.toString = function() {
        return this.name + " " + this.credits + " " + this.gpa;
    }
}

pastClass.prototype = Class.prototype;
pastClass.prototype.constructor = pastClass;

function calculateGPA(args) {
    var grades_creds = 0;
    this.total = 0;
    this.args = args;
    for (var arg in this.args) {
        grades_creds += this.args[arg].gpa*this.args[arg].credits;
        this.total += this.args[arg].credits;
    }
    this.gpa = grades_creds/this.total;
}