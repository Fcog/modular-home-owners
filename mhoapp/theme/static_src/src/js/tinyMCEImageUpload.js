export default function tinyMCEImageUpload(blobInfo, success, failure, progress) {
    var xhr, formData

    xhr = new XMLHttpRequest()
    xhr.withCredentials = false
    xhr.open('POST', '/upload_image/')

    xhr.upload.onprogress = function (e) {
        progress(e.loaded / e.total * 100)
    }

    xhr.onload = function() {
        var json

        if (xhr.status === 403) {
            failure('HTTP Error: ' + xhr.status, { remove: true })
            return
        }

        if (xhr.status < 200 || xhr.status >= 300) {
            console.log('status >= 300')
            failure('HTTP Error: ' + xhr.status)
            return
        }

        json = JSON.parse(xhr.responseText)

        if (!json || typeof json.location != 'string') {
            failure('Invalid JSON: ' + xhr.responseText)
            return
        }

        if (json.error) {
            failure(json.message)
            return
        }        

        success(json.location)
    }

    xhr.onerror = function () {
        failure('Image upload failed due to a XHR Transport error. Code: ' + xhr.status)
        return
    }

    formData = new FormData()
    formData.append('file', blobInfo.blob(), blobInfo.filename())

    xhr.send(formData)
}