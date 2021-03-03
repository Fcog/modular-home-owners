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
            }
        ]
    },

    devServer: {
        contentBase: path.resolve(__dirname, 'dist'),
        writeToDisk: true,
    },
}