class UserAPI {
    location = 'http://localhost:7279/User/'

    //POST auth
    async auth(login, password) {
        return await fetch(this.location + 'Login' + '?login=' + login + '&password=' + password, {method: 'post'})
            .then(res => {
                return true
            })
            .catch(error => {
                return error
            })
    }

    //POST /:id
    async register({product_id}) {
        return await fetch(this.location + 'register', {method: 'post'}).then(res => res.json())
    }

}

export default new UserAPI()