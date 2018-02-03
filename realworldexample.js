const https = require("https");

const urlList = [
  "https://reqres.in/api/users?page=1",
  "https://reqres.in/api/users?page=2",
  "https://reqres.in/api/users?page=3"
];

function getSiteContents(url) {
  return new Promise(function (resolve, reject) {
    https.get(url, function (res) {
      var bodyData = "";
      res.on("data", function (chunk) {
        bodyData += chunk;
      });
      res.on("end", function () {
        resolve(bodyData);
      });
      res.on("error", function (error) {
        reject(error.message);
      });
    }); 
  });
}

Promise.all(urlList.map(getSiteContents)).then(function (siteContents) {
  console.log(siteContents);
});
