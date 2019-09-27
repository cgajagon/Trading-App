var path = require("path");
var webpack = require('webpack');
var BundleTracker = require('webpack-bundle-tracker');
const MiniCssExtractPlugin = require('mini-css-extract-plugin');

module.exports = {
    context: __dirname,

    entry: {
        index:'./trading/static/js/index',
    },

    output: {
        path: path.resolve('./trading/static/bundles/'),
        filename: "[name]-[hash].js",
    },

    plugins: [
        new BundleTracker({ filename: './webpack-stats.json' }),
        new MiniCssExtractPlugin({
            filename: '[name]-[hash].css',
            chunkFilename: '[id].css',
          }),
    ],
    module: {
        rules: [
            {
                test: /\.scss$/,
                use: [
                    MiniCssExtractPlugin.loader,
                    {loader:"css-loader"},
                    {
                        loader: 'sass-loader',
                        options: {
                            sassOptions: {
                                includePaths: ['./node_modules']
                        }
                      }                
                    }
                ]
            }
        ]
    },
};