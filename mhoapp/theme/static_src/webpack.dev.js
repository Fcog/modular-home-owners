const { merge } = require('webpack-merge');
const common = require('./webpack.common.js');

module.exports = merge(common, {
    mode: 'development',
    devtool: 'inline-source-map',
    devServer: {
        contentBase: path.resolve(__dirname, './../static/mhoapp'),
        writeToDisk: true,
        injectClient: false,
        socket: 'socket',
    },
});