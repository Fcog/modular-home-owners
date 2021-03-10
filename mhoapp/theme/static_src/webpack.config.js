const path = require("path");
const MiniCssExtractPlugin = require('mini-css-extract-plugin');

module.exports = {
    mode: 'production',
    entry: './src/index.js',
    output: {
        path: path.resolve(__dirname, './../static/mhoapp'),
        filename: 'bundle.js'
    },

    plugins: [
        new MiniCssExtractPlugin()
    ],

    module: {
        rules: [
            {
                test: /\.js$/i,
                include: path.resolve(__dirname, 'src'),
                use: {
                    loader: 'babel-loader',
                    options: {
                        presets: ['@babel/preset-env'],
                    },
                },
            },
            {
                test: /\.css$/i,
                // Chains from last to fist.
                use: [
                    MiniCssExtractPlugin.loader,
                    'css-loader', // Read and imports the CSS from the CSS files.
                    'postcss-loader',
                ]
            },
            {
                test: /\.(jpe?g|png|gif|woff|woff2|eot|ttf|svg)(\?[a-z0-9=.]+)?$/,
                use: {
                    loader: 'url-loader?limit=100000'
                }
            }
        ]
    },

    devServer: {
        contentBase: path.resolve(__dirname, 'dist'),
        writeToDisk: true,
    },
}