exports.config = {
    directConnect: true,
    capabilities:
    {
        'browserName': 'chrome'
    },
    framework: 'jasmine',
    specs: ['..//JASMINE//SmartTest.js'],
    jasmineNodeOpts:
    {
        defualtTimeoutInterval: 30000
    }
};