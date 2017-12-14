# -*-coding:utf-8 -*-
# Created by Helic on 17-5-10
import numpy
import time
import sys
import subprocess
import os
import random
import theano
import json

sys.path.append('..')
from theano import tensor as T


class RNN(object):
    def __init__(self, nh, nc, ne, de, cs):
        '''
        nh :: dimension of the hidden layer
        nc :: number of classes                                           iob种类
        ne :: number of word embeddings in the vocabulary                  词表大小
        de :: dimension of the word embeddings
        cs :: word window context size
        '''
        # parameters of the model
        self.emb = theano.shared(numpy.load('./NLU/data/trained_model/embeddings.npy').astype(
            theano.config.floatX))  # add one for PADDING at the end, emb is a (ne+1)*de matrix
        self.Wx = theano.shared(numpy.load('./NLU/data/trained_model/Wx.npy').astype(theano.config.floatX))  # (de * cs)*nh
        self.Wh = theano.shared(numpy.load('./NLU/data/trained_model/Wh.npy').astype(theano.config.floatX))
        self.W = theano.shared(numpy.load('./NLU/data/trained_model/W.npy').astype(theano.config.floatX))
        self.bh = theano.shared(numpy.load('./NLU/data/trained_model/bh.npy').astype(theano.config.floatX))
        self.b = theano.shared(numpy.load('./NLU/data/trained_model/b.npy').astype(theano.config.floatX))
        self.h0 = theano.shared(numpy.load('./NLU/data/trained_model/h0.npy').astype(theano.config.floatX))

        # bundle
        self.params = [self.emb, self.Wx, self.Wh, self.W, self.bh, self.b, self.h0]
        self.names = ['embeddings', 'Wx', 'Wh', 'W', 'bh', 'b', 'h0']
        idxs = T.imatrix()  # 矩阵，行数等于句子里面单词数目，列数等于窗大小
        # print(idxs)                                         # <TensorType(int32, matrix)>
        x = self.emb[idxs].reshape((idxs.shape[0], de * cs))  # x is a matrix 句子里面单词数目*(de*cs) ,int32
        # print self.emb[idxs]
        y = T.iscalar('y')  # label

        # 递归
        def recurrence(x_t, h_tm1):
            h_t = T.nnet.sigmoid(T.dot(x_t, self.Wx) + T.dot(h_tm1, self.Wh) + self.bh)
            s_t = T.nnet.softmax(T.dot(h_t, self.W) + self.b)
            return [h_t, s_t]

        [h, s], _ = theano.scan(fn=recurrence, sequences=x, outputs_info=[self.h0, None], n_steps=x.shape[0])
        p_y_given_x_sentence = s[:, 0, :]
        y_pred = T.argmax(p_y_given_x_sentence, axis=1)

        # 分类，训练函数
        self.classify = theano.function(inputs=[idxs], outputs=y_pred)






