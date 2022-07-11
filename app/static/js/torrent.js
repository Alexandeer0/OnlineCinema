const client = new WebTorrent()

const torrentId = 'magnet:?xt=urn:btih:08ada5a7a6183aae1e09d831df6748d566095a10&dn=Sintel&tr=udp%3A%2F%2Fexplodie.org%3A6969&tr=udp%3A%2F%2Ftracker.coppersurfer.tk%3A6969&tr=udp%3A%2F%2Ftracker.empire-js.us%3A1337&tr=udp%3A%2F%2Ftracker.leechers-paradise.org%3A6969&tr=udp%3A%2F%2Ftracker.opentrackr.org%3A1337&tr=wss%3A%2F%2Ftracker.btorrent.xyz&tr=wss%3A%2F%2Ftracker.fastcast.nz&tr=wss%3A%2F%2Ftracker.openwebtorrent.com&ws=https%3A%2F%2Fwebtorrent.io%2Ftorrents%2F&xs=https%3A%2F%2Fwebtorrent.io%2Ftorrents%2Fsintel.torrent'

client.add(torrentId, function (torrent) {
  // Torrents can contain many files. Let's use the .mp4 file
  const file = torrent.files.find(function (file) {
    return file.name.endsWith('.mp4')
  })
  const poster = torrent.files.find(function (file) {
    return file.name.endsWith('.jpg')
  })
  // document.querySelector('video').poster = poster
  
  file.renderTo('video')
  // file.getBlobURL(function (err, url) {
  //     if (err) return console.log(err.message)
  //   // log('<a href="' + url + '">Download full file: ' + file.name + '</a>')

  //   const source = document.createElement('source')
  //   console.log(source)
  //   source.src = url
  //   // source.type="video/mp4"
  //   document.querySelector('video').appendChild(source)
  // })
})

        
        
        
        
        


        // client.on('error', function (err) {
        //     console.error('ERROR: ' + err.message)
        // })
